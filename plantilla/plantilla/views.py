from django.shortcuts import render

def simple(requets):
  return render(requets, 'simple.html', {})

def personal(requets, name, age):
  context = {
    'name': name,
    'age': age,
    'categories': [
      'html', 'css', 'python', 'git', 'javascript'
    ]
  }
  return render(requets, 'personal.html', context)