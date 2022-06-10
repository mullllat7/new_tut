from django.contrib import admin

from app.course.models import Course, CourseImage, Saved, Like


class InlineCourseImage(admin.TabularInline):
    model = CourseImage
    extra = 1
    fields = ['image', ]


class CourseAdminDisplay(admin.ModelAdmin):
    inlines = [InlineCourseImage, ]


class LikeAdmin(admin.ModelAdmin):
    list_display = ('author', 'course',)
    list_display_links = ('author', 'course')
    search_fields = ['author', 'course',]
    list_filter = ('author', 'course',)


admin.site.register(Course, CourseAdminDisplay)
admin.site.register(Like, LikeAdmin)
admin.site.register(Saved)
admin.site.register(CourseImage)

