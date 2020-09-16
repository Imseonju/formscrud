from django.shortcuts import render, get_object_or_404, redirect
from .models import Board
from .forms import BoardForm
from datetime import datetime

def boardlist(request):
    boards = Board.objects.all()
    return render(request, 'boardlist.html', {'boards': boards})

def show(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'show.html', {'board':board})

def new(request):
    return render(request, 'new.html')

def boardcreate(request):
        if request.method == 'POST':
            form = BoardForm(request.POST)
            if form.is_valid():
                board = form.save(commit=False)
                board.create_at = datetime.now()
                board.save()
                return redirect('boardlist')
            else:
                return redirect('boardlist')
        else:
            form = BoardForm()
            return render(request, 'new.html', {'form':form})

def edit(request):
    return render(request, 'edit.html')

def boardupdate(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.save()
            return redirect('show', pk=board.pk)
        else:
            return redirect('boardlist')
    else:
        form = BoardForm(instance=board)
        return render(request, 'edit.html', {'form':form})

def boarddelete(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board.delete()
    return redirect('boardlist')