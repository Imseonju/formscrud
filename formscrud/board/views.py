from django.shortcuts import render, get_object_or_404, redirect
from .models import Board
from .forms import BoardForm
from datetime import datetime

def boardlist(request):
    return render(request, 'boardlist.html')

def show(request, board_id):
    return render(request, 'show.html')

def new(request):
    return render(request, 'new.html')

def boardcreate(request):
        if request.method == 'POST':
            form = BoardForm(request.POST)
            if form.is_valid():
                board = form.save(commit=False)
                board.create_at = datetime.now
                board.save()
                return redirect('boardlist')
            else:
                return redirect('boardlist')
        else:
            form = BoardForm()
            return render(request, 'new.html', {'form':form})

def edit(request):
    return render(request, 'edit.html')

def boardupdate(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=post)
        if form.is_valid():
            board = form.save(commit=False)
            board.save()
            return redirect('show', board_id=board.pk)
        else:
            return redirect('boardlist')
    else:
        form = BoardForm(instance=post)
        return render(request, 'edit.html', {'form':form})

def boarddelete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    board.delete()
    return redirect('boardlist')