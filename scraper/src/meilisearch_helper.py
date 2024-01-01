class MeiliSearchHelper:
    def __init__(self, config, index_uid):
        self.config = config
        self.uid = index_uid
        self.meilisearch_index = None

    def delete_index(self):
        try:
            self.meilisearch_index.delete("http://"+f"{self.config.paths.index}/{self.uid}")
        except requests.exceptions.MissingSchema:
            self.meilisearch_index.delete("https://"+f"{self.config.paths.index}/{self.uid}")
