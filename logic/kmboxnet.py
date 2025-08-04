from __future__ import annotations

try:
    import kmNet  # type: ignore
except Exception:  # pragma: no cover - library is optional
    kmNet = None

from logic.config_watcher import cfg
from logic.logger import logger


class KmboxNet:
    def __init__(self, host: str, port: int, uuid: str) -> None:
        self.host = host
        self.port = port
        self.uuid = uuid

        if kmNet is None:
            logger.error("[KmboxNet] kmNet library not available")
            return

        try:
            kmNet.init(host, port, uuid)
            kmNet.monitor(5001)
        except Exception as e:  # pragma: no cover - hardware specific
            logger.error(f"[KmboxNet] Init failed: {e}")

    def move(self, x: int, y: int) -> None:
        if kmNet is None:
            return
        try:
            kmNet.move(int(x), int(y))
        except Exception as e:  # pragma: no cover - hardware specific
            logger.error(f"[KmboxNet] Move failed: {e}")

    def press(self) -> None:
        if kmNet is None:
            return
        try:
            kmNet.left(1)
        except Exception as e:  # pragma: no cover - hardware specific
            logger.error(f"[KmboxNet] Press failed: {e}")

    def release(self) -> None:
        if kmNet is None:
            return
        try:
            kmNet.left(0)
        except Exception as e:  # pragma: no cover - hardware specific
            logger.error(f"[KmboxNet] Release failed: {e}")


kmbox = KmboxNet(cfg.kmboxnet_host, cfg.kmboxnet_port, cfg.kmboxnet_uuid)

