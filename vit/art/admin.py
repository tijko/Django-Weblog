from django.contrib import admin
from vit.art.models import *

admin.site.register(Post, PostAdmin)
admin.site.register(Index, IndexAdmin)
admin.site.register(Comment, CommentAdmin)
