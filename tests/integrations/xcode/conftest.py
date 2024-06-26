from unittest.mock import MagicMock

import pytest

from briefcase.integrations.base import ToolCache
from briefcase.integrations.file import File
from briefcase.integrations.subprocess import Subprocess


@pytest.fixture
def mock_tools(tmp_path, mock_tools) -> ToolCache:
    mock_tools.host_os = "Darwin"

    # Mock default tools
    mock_tools.subprocess = MagicMock(spec_set=Subprocess)
    mock_tools.file.download = MagicMock(spec_set=File.download)

    return mock_tools
