import telegram
from django.conf import settings
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Book
import asgiref.sync

# Создание бота Telegram
bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)

# Асинхронная функция для отправки сообщений в Telegram
async def send_telegram_message(message):
    chat_id = settings.TELEGRAM_CHAT_ID
    await bot.send_message(chat_id=chat_id, text=message)

# Функция-обертка для запуска асинхронной функции в синхронном контексте
def run_async(func):
    asgiref.sync.async_to_sync(func)()

# Обработчик сигнала сохранения модели Book
@receiver(post_save, sender=Book)
def handle_book_save(sender, instance, created, **kwargs):
    if created:
        message = f"Новая книга создана: {instance.title}"
    else:
        message = f"Книга обновлена: {instance.title}"
    run_async(lambda: send_telegram_message(message))

# Обработчик сигнала удаления модели Book
@receiver(pre_delete, sender=Book)
def handle_book_delete(sender, instance, **kwargs):
    message = f"Книга удалена: {instance.title}"
    run_async(lambda: send_telegram_message(message))