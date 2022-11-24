from django.shortcuts import render
from django.http import HttpResponse
import tensorflow as tf


def random_num():
    temp = tf.random.Generator.from_seed(1)
    return temp.normal(shape=(1,3))

# Create your views here.
def index(request):
    print(random_num().numpy())
    return HttpResponse("Sdf")