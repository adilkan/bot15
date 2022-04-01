import hashlib
from aiogram import types, Dispatcher

async def inline_wiki(query: types.InlineQuery):
    text = query.query or "echo"
    links= "https://www.google.com/search?q=" + text
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    articles = [
        types.InlineQueryResultArticle(
            id=result_id,
            title="google:",
            url=links,
            input_message_content=types.InputTextMessageContent(
                message_text=links

            )
        )
    ]
    await query.answer(articles, cache_time=2, is_personal=True)


def register_handlers_inline(db: Dispatcher):
    db.register_inline_handler(inline_wiki)