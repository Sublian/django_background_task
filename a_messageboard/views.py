import threading
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from .models import MessageBoard
from .forms import MessageCreateForm
from .tasks import send_email_task


@login_required
def messageboard_view(request):
    messageboard = get_object_or_404(MessageBoard, id=1)
    form = MessageCreateForm()

    if request.method == "POST":
        if request.user in messageboard.subscribers.all():
            form = MessageCreateForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.author = request.user
                message.messageboard = messageboard
                message.save()
                send_email(message)

        else:
            messages.warning(request, "You must be a subscriber to post messages.")
        return redirect("messageboard")

    context = {"messageboard": messageboard, "form": form}
    return render(request, "a_messageboard/index.html", context)


@login_required
def subscribe(request):
    messageboard = get_object_or_404(MessageBoard, id=1)
    if request.user not in messageboard.subscribers.all():
        messageboard.subscribers.add(request.user)
    else:
        messageboard.subscribers.remove(request.user)
    return redirect("messageboard")


def send_email(message):
    messageboard = message.messageboard
    subscribers = messageboard.subscribers.all()

    for subscriber in subscribers:
        subject = f"New Message Posted from {message.author.profile.name}"
        body = f"{message.author.profile.name}: {message.body}\n\nVisit the messageboard to see more."

        send_email_task.delay(subject, body, subscriber.email)


#         # Using threading to send email asynchronously
#         email_thread = threading.Thread(target=send_email_thread, args=(subject, body, subscriber))
#         email_thread.start()

# def send_email_thread(subject, body, subscriber):
#     email = EmailMessage(
#         subject,
#         body,
#         to=[subscriber.email]
#     )
#     email.send()
