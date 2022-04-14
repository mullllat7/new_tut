from django.contrib import admin

from app.lesson.models import Lesson, Video


class InlineLessonVideo(admin.TabularInline):
    model = Video
    extra = 1
    fields = ['video', ]


class LessonsAdminDisplay(admin.ModelAdmin):
    inlines = [InlineLessonVideo, ]


admin.site.register(Lesson, LessonsAdminDisplay)
