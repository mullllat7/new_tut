from django.contrib import admin

from app.course.models import Course, CourseImage, Saved


class InlineCourseImage(admin.TabularInline):
    model = CourseImage
    extra = 1
    fields = ['image', ]


class CourseAdminDisplay(admin.ModelAdmin):
    inlines = [InlineCourseImage, ]


admin.site.register(Course, CourseAdminDisplay)
admin.site.register(Saved)

