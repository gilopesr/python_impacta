from time import perf_counter, sleep

def cronometro(f):
    def envelope():
        t1 = perf_counter()
        f()
        t2 = perf_counter()
        print(f'{f.__name__} executada em {t2-t1:.3e} segundos')
    return envelope


def funcao_exemplo():
    print('esperando 2 segundos')
    sleep(2)
    
funcao_exemplo = cronometro(funcao_exemplo)
funcao_exemplo()