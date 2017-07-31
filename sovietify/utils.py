def sovietify(text):

    output = ''
    vocab = dict(A = 'Д', a = 'д', B = 'В', b = 'в', C = 'С', c = 'с', E = 'Е', e = 'е', H = 'Н', h = 'н', K = 'К', k = 'к', M = 'М', m = 'м', N = 'И', n = 'и', O = 'О', o = 'о', P = 'Р', p = 'р', R = 'Я', r = 'г', T = 'Т', t = 'т', X = 'Х', x = 'х', Y = 'У', y = 'у')
    for char in text:
        if char in vocab:
            output += vocab[char]
        else:
            output += char

    return output