from aiogram import types, Dispatcher
import hashlib

async def inline_wikipedia_handler(query: types.InlineQuery):
    text = query.query or "echo"
    link = f"https://ru.wikipedia.org/wiki/{text}"
    articles = [types.InlineQueryResultArticle(
        id=hashlib.md5(text.encode()).hexdigest(),
        title='wikipedia: ',
        url=link,
        input_message_content=types.InputMessageContent(
            message_text=link
        )
    )]
    await query.answer(articles, cache_time=60)


def register_inline_handler(dp: Dispatcher):
    # dp.register_inline_handler(inline_youtube_handler)
    dp.register_inline_handler(inline_wikipedia_handler)