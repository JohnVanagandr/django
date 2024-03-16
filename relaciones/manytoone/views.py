from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Post
from datetime import date
# Create your views here.

def create(request):
  repo = Reporter(first_name='John', last_name='Becerra', email='jfbecerra@sena.edu.co')
  repo.save()

  post1 = Post(headline="Django básico", date=date(2024,3,4), reporter= repo)
  post2 = Post(headline="Django intermedio", date=date(2024,4,4), reporter= repo)
  post3 = Post(headline="Django avanzado", date=date(2024,5,4), reporter= repo)

  post1.save()
  post2.save()
  post3.save()

  # query = post1.reporter.first_name
  query = repo.post_set.all()

  return HttpResponse(query)
