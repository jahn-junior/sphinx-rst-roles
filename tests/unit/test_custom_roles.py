# This file is part of sphinx-ext-template.
#
# Copyright 2025 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License version 3, as published by the Free
# Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranties of MERCHANTABILITY, SATISFACTORY
# QUALITY, or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

import pytest
from docutils import nodes
from rst_roles.roles import LiteralrefRole, NoneRole, SpellExceptionRole
from typing_extensions import override


class FakeSpellExceptionRole(SpellExceptionRole):
    @override
    def __init__(self, text):
        self.text = text


class FakeNoneRole(NoneRole):
    @override
    def __init__(self, text):
        self.text = text


class FakeLiteralrefRole(LiteralrefRole):
    @override
    def __init__(self, text):
        self.text = text


@pytest.fixture
def fake_spellexception_role(request: pytest.FixtureRequest) -> FakeSpellExceptionRole:
    """This fixture can be parametrized to override the default values."""
    # Get any optional overrides from the fixtures
    overrides = request.param if hasattr(request, "param") else {}

    return FakeSpellExceptionRole(text=overrides.get("text", []))


@pytest.fixture
def fake_none_role(request: pytest.FixtureRequest) -> FakeNoneRole:
    """This fixture can be parametrized to override the default values."""
    # Get any optional overrides from the fixtures
    overrides = request.param if hasattr(request, "param") else {}

    return FakeNoneRole(text=overrides.get("text", []))


@pytest.fixture
def fake_literalref_role(request: pytest.FixtureRequest) -> FakeLiteralrefRole:
    """This fixture can be parametrized to override the default values."""
    # Get any optional overrides from the fixtures
    overrides = request.param if hasattr(request, "param") else {}

    return FakeLiteralrefRole(text=overrides.get("text", []))


@pytest.mark.parametrize(
    "fake_none_role",
    [{"text": ["this does nothing."]}],
    indirect=True,
)
def test_none_role(fake_none_role: FakeNoneRole):
    expected: tuple[list[nodes.Node], list[nodes.system_message]] = [], []
    actual = fake_none_role.run()

    assert expected == actual
