from telegram import Update
from telegram.ext import Updater, MessageHandler, filters, CallbackContext, ApplicationBuilder

# 删除加入和退出消息的回调函数
async def delete_join_leave(update: Update, context: CallbackContext) -> None:
    # 检查消息是否为加入或退出消息
    if update.message.new_chat_members or update.message.left_chat_member:
        # 删除消息
        await context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)

# 主函数，设置和启动机器人
def main():
    # 将 'YOUR_BOT_TOKEN' 替换为你的 Telegram bot token
    application = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    # 添加一个消息处理器，过滤加入和退出消息
    join_leave_handler = MessageHandler(filters.StatusUpdate.ALL, delete_join_leave)
    application.add_handler(join_leave_handler)

    # 启动机器人
    application.run_polling()

if __name__ == '__main__':
    main()
  
