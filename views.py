from django.shortcuts import render
from .models import Bb
from .models import Rubric
from django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from .models import Product
from .forms import ProductForm, ProductMetaFormSet
from django.shortcuts import render, redirect, get_object_or_404
import asyncio
from django.http import JsonResponse


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)

def rubric_bbs(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics,
    'current_rubric': current_rubric}
    return render(request, 'bboard/rubric_bbs.html', context)

class BbCreateView(CreateView):
    template_name = 'bboard/bb_create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['rubrics'] = Rubric.objects.all()
    return context

class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'bboard/product_list.html', {'products': products})

class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        formset = ProductMetaFormSet()
        return render(request, 'bboard/product_form.html', {'form': form, 'formset': formset})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        formset = ProductMetaFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            product = form.save()
            metas = formset.save(commit=False)
            for m in metas:
                m.product = product
                m.save()
            for m in formset.deleted_objects:
                m.delete()
            return redirect('bboard:product_list')
        return render(request, 'bboard/product_form.html', {'form': form, 'formset': formset})


class ProductUpdateView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        formset = ProductMetaFormSet(instance=product)
        return render(request, 'bboard/product_form.html', {
            'form': form,
            'formset': formset,
            'product': product,
        })

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=product)
        formset = ProductMetaFormSet(request.POST, instance=product)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('bboard:product_list')
        return render(request, 'bboard/product_form.html', {
            'form': form,
            'formset': formset,
            'product': product,
        })

class ProductDeleteView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()          # удалит и связанные ProductMeta по CASCADE
        return redirect('bboard:product_list')

async def async_test(request):
    await asyncio.sleep(1)  # имитация долгой операции
    return JsonResponse({'status': 'ok', 'message': 'async view works'})
