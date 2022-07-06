from django.contrib import admin

from app.lesson.models import Lesson, Video


# class InlineLessonVideo(admin.TabularInline):
#     model = Video
#     extra = 0
#     fields = ['video', ]


# class LessonsAdminDisplay(admin.ModelAdmin):
#     inlines = [InlineLessonVideo, ]


# admin.site.register(Lesson, LessonsAdminDisplay)
# # admin.site.register(Lesson)



class InlineLessonVideo(admin.TabularInline):
    model = Video
    fields = ('video', )
    max_num = 1                                 
                                                
@admin.register(Lesson)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        InlineLessonVideo
    ]