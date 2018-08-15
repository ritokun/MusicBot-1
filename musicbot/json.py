import json
import logging

log = logging.getLogger(__name__)

class Json:
    def __init__(self, json_file):
        log.debug('Init JSON obj with {0}'.format(json_file))
        self.file = json_file
        self.data = self.parse()

    def parse(self):
        """JSONとしてファイルを解析する"""
        with open(self.file, encoding='utf-8') as data:
            try:
                parsed = json.load(data)
            except Exception:
                log.error('JSONとして{0}を解析中にエラーが発生しました'.format(self.file), exc_info=True)
        return parsed

    def get(self, item, fallback=None):
        """JSONファイルから項目を取得します。"""
        try:
            data = self.data[item]
        except KeyError:
            log.warning('i18nキー{0}からデータを取得できませんでした。'.format(item, fallback))
            data = fallback
        return data
