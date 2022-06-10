import logging


def log(func):

    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # Открываем файл логов для записи.
        fh = logging.FileHandler("%s.log" % name)
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info("Call function: %s" % name)
        result = func(*args, **kwargs)
        logger.info("Result: %s" % result)
        return func

    return wrap_log


@log
def double_function(a):
    return a ** 2


value = double_function(5)