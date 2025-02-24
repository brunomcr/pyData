import logging

def setup_logging(level=logging.INFO):
    """Configura o logging básico para o projeto."""
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=level
    ) 