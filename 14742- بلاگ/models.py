# بلاگ
# ID : 14742
# https://quera.org/problemset/14742


from django.db import models

# TODO write all of your code here...

class Author(models.Model):
	name = models.CharField(max_length=50)

class BlogPost(models.Model):
	title = models.CharField(max_length = 250)
	body = models.TextField()
	author = models.ForeignKey(Author, on_delete= models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)


	def copy(self):
		BP = BlogPost()
		BP.title = self.title
		BP.body = self.body
		BP.author = self.author
		BP.save()
		CM = self.comment_set.all()
		
		for c in CM:
			CO = Comment()
			CO.blog_post = BP
			CO.text = c.text
			CO.save()

		return BP.id
		

		

class Comment(models.Model):
	blog_post = models.ForeignKey(BlogPost, on_delete= models.CASCADE)
	text = models.CharField(max_length = 500)
		
