import logging


def make_function(name: str = None):
    logger = logging.getLogger(name)
    logging.basicConfig(format="%(asctime)s | %(name)s | %(levelname)s - %(message)s")

    def wrapper(log_level):
        level_func = getattr(logger, log_level)

        def alternative_logging(msg, *args):
            nonlocal level_func
            level_func(msg)
            # add some actions, maybe with args

        return alternative_logging

    return map(wrapper, ('debug', 'info', 'warning', 'error', 'critical'))


debug, info, warning, error, critical = make_function('Nice name')
debug2, info2, warning2, error2, critical2 = make_function('Bad name')


warning('oh no')
warning2('what is it')
error('hold on')
error2('are ya ok')
critical('ded')
critical2('not big surprise')
