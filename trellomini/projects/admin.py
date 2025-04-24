from django.contrib import admin, messages
from .models import Project, Task
from django.utils.translation import ngettext


class TasksInline(admin.TabularInline):
    model = Task
    fields = ('title', 'status', 'assignee')
    extra = 0

# Register models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'updated_at', 'created_at')
    list_filter = ('owner', 'created_at', 'updated_at')
    search_fields = ('name', 'owner__username')
    inlines = [TasksInline]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'assignee', 'updated_at', 'created_at')
    list_filter = ('project', 'status', 'assignee', 'updated_at', 'created_at')
    actions = ['markDone', 'markDoing', 'markToDo']
    ordering = ('-project',)

    @admin.action(description="Mark selected tasks as done")
    def markDone(self, request, queryset):
        amountUpdated = queryset.update(status = 'DONE')
        # for task in queryset:
        #     task.status = 'DONE'
        #     task.save()
        self.message_user(
            request,
            ngettext(
                '%d task marked as "done" successfully.',
                '%d tasks marked as "done" successfully.',
                amountUpdated
            )
            % amountUpdated,
            messages.SUCCESS
        )

    @admin.action(description="Mark selected tasks as doing")
    def markDoing(self, request, queryset):
        amountUpdated = queryset.update(status = 'DOING')
        self.message_user(
            request,
            ngettext(
                '%d task marked as "doing" successfully.',
                '%d tasks marked as "doing" successfully.',
                amountUpdated
            )
            % amountUpdated,
            messages.SUCCESS
        )

    @admin.action(description="Mark selected tasks as todo")
    def markToDo(self, request, queryset):
        amountUpdated = queryset.update(status = 'TODO')
        self.message_user(
            request,
            ngettext(
                '%d task marked as "todo" successfully.',
                '%d tasks marked as "todo" successfully.',
                amountUpdated
            )
            % amountUpdated,
            messages.SUCCESS
        )

