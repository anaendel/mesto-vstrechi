def get_poem_body(text):
    """Убирает первую строку (название) из текста стихотворения."""
    lines = text.strip().splitlines()
    rest = lines[1:]
    while rest and not rest[0].strip():
        rest = rest[1:]
    return '\n'.join(rest)


def get_poem_preview(text):
    """Возвращает первую строку стихотворения (не название) + многоточие."""
    body = get_poem_body(text)
    for line in body.splitlines():
        if line.strip():
            clean_line = line.strip().rstrip('...,.;:!?—-')
            return clean_line + '...'
    return '...'