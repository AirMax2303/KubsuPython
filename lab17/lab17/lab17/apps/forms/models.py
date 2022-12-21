from django.db import models


class Form(models.Model):
    form_title = models.CharField('Название формы', max_length=200)
    form_text = models.TextField('Текст формы')
    pub_date = models.DateTimeField('Дата публикации')


class Comment(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=200)
    comment_text = models.CharField('Текс комментария', max_length=200)
