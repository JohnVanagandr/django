from django.shortcuts import render
from django.http import HttpResponse

from .models import Article, Publication

# Create your views here.

def create(request):
  # art1 = Article(headline="Primer articulo")
  # art2 = Article(headline="Segundo articulo")
  # art3 = Article(headline="Tercero articulo")
  # art1.save()
  # art2.save()
  # art3.save()

  # pub1 = Publication(title="Publicación uno")
  # pub2 = Publication(title="Publicación dos")
  # pub3 = Publication(title="Publicación tres")
  # pub4 = Publication(title="Publicación cuarta")
  # pub5 = Publication(title="Publicación quinta")
  # pub6 = Publication(title="Publicación sexta")
  
  # pub1.save()
  # pub2.save()
  # pub3.save()
  # pub4.save()
  # pub5.save()
  # pub6.save()

  #relacionamos los modelos
  # art1.Publications.add(pub1)
  # art1.Publications.add(pub2)
  # art1.Publications.add(pub3)

  # art2.Publications.add(pub4)
  # art2.Publications.add(pub5)

  # art3.Publications.add(pub6)

  # art1 = Article.objects.get(id=1)
  # result = art1.Publications.all()

  # consulta inversa
  # pub1 = Publication.objects.get(id=1)
  # result = pub1.article_set.all()

  # Para poder remover o eliminar una relación
  
  art3 = Article.objects.get(id=3)
  pub6 = Publication.objects.get(id=6)
  art3.Publications.remove(pub6)

  return HttpResponse(art3)