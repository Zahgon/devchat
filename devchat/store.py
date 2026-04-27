import json
import os
from dataclasses import asdict
from typing import Any, Dict, List, Optional

from tinydb import Query, TinyDB, where
from tinydb.table import Table

from devchat.chat import Chat
from devchat.prompt import Prompt
from devchat.utils import get_logger

logger = get_logger(__name__)


class Store:
    def __init__(self, store_dir: str, chat: Chat):
        """
        Initializes a Store instance.

        Args:
            store_dir (str): The folder to store the files containing the store.
            chat (Chat): The Chat instance.
        """
        store_dir = os.path.expanduser(store_dir)
        if not os.path.isdir(store_dir):
            os.makedirs(store_dir)

        self._graph_path = os.path.join(store_dir, "prompts.graphml")
        self._chat_list_path = os.path.join(store_dir, "prompts_list.json")
        self._db_path = os.path.join(store_dir, "prompts.json")
        self._chat = chat

        self._db = TinyDB(self._db_path)
        self._db_meta = self._migrate_db()
        self._topics_table = self._db.table("topics")

        if os.path.isfile(self._chat_list_path):
            with open(self._chat_list_path, "r", encoding="utf-8") as file:
                self._chat_lists = json.loads(file.read())
        elif os.path.isfile(self._graph_path):
            # convert old graphml to new json
            from xml.etree.ElementTree import ParseError

            import networkx as nx

            try:
                graph = nx.read_graphml(self._graph_path)

                roots = [node for node in graph.nodes() if graph.out_degree(node) == 0]

                self._chat_lists = []
                for root in roots:
                    chat_list = [(root, graph.nodes[root]["timestamp"])]

                    ancestors = nx.ancestors(graph, root)
                    for ancestor in ancestors:
                        chat_list.append((ancestor, graph.nodes[ancestor]["timestamp"]))

                    self._chat_lists.append(chat_list)

                with open(self._chat_list_path, "w", encoding="utf-8") as file:
                    file.write(json.dumps(self._chat_lists))

                # rename graphml to json
                os.rename(self._graph_path, self._graph_path + ".bak")

                # update topic table, add request and response fields
                # new fields: user, date, request, responses, hash
                visible_topics = self._topics_table.all()
                for topic in visible_topics:
                    prompt = self.get_prompt(topic["root"])
                    if not prompt:
                        continue
                    self._update_topic_fields(topic, prompt)
                    self._topics_table.update(topic, doc_ids=[topic.doc_id])

            except ParseError as error:
                raise ValueError(f"Invalid file format for graph: {self._graph_path}") from error
        else:
            self._chat_lists = []

        if not self._topics_table or not self._topics_table.all():
            self._initialize_topics_table()

    def _update_topic_fields(self, topic, prompt):
        pass

    def _migrate_db(self) -> Table:
        """
        Migrate the database to the latest version.
        """
        pass

    def _initialize_topics_table(self):
        pass

    def _update_topics_table(self, prompt: Prompt):
        pass

    def store_prompt(self, prompt: Prompt) -> str:
        """
        Store a prompt in the store.

        Args:
            prompt (Prompt): The prompt to store.
        """
        pass

    def get_prompt(self, prompt_hash: str) -> Prompt:
        """
        Retrieve a prompt from the store.

        Args:
            prompt_hash (str): The hash of the prompt to retrieve.
        Returns:
            Prompt: The retrieved prompt. None if the prompt is not found.
        """
        pass

    def select_prompts(self, start: int, end: int, topic: Optional[str] = None) -> List[Prompt]:
        """
        Select recent prompts in reverse chronological order.

        Args:
            start (int): The start index.
            end (int): The end index (excluded).
            topic (Optional[str]): The hash of the root prompt of the topic.
                If set, select among the prompts of the topic.
        Returns:
            List[Prompt]: The list of prompts selected.
                If end is greater than the number of all prompts,
                the list will contain prompts from start to the end of the list.
        """
        pass

    def select_topics(self, start: int, end: int) -> List[Dict[str, Any]]:
        """
        Select recent topics in reverse chronological order.

        Args:
            start (int): The start index.
            end (int): The end index (excluded).

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing root prompts
                with latest_time, and title fields.
        """
        pass

    def delete_prompt(self, prompt_hash: str) -> bool:
        """
        Delete a prompt from the store if it is a leaf.

        Args:
            prompt_hash (str): The hash of the prompt to delete.

        Returns:
            bool: True if the prompt is successfully deleted, False otherwise.
        """
        pass

    @property
    def graph_path(self) -> str:
        """
        The path to the graph store file.
        """
        pass

    @property
    def db_path(self) -> str:
        """
        The path to the object store file.
        """
        pass
