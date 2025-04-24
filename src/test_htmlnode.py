import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
	def test_props_to_html_none(self):
		node = HTMLNode(props=None)
		self.assertEqual(node.props_to_html(), "")

	def test_props_to_html_empty(self):
		node = HTMLNode(props = {})
		self.assertEqual(node.props_to_html(), "")

	def test_props_to_html_single_prop(self):
		node = HTMLNode(props={"href": "https://example.com"})
		self.assertEqual(node.props_to_html(), ' href="https://example.com"')


	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, World!")
		self.assertEqual(node.to_html(),"<p>Hello, World!</p>")

	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
		self.assertEqual(
			node.to_html(),
			'<a href="https://www.google.com">Click me!</a>', )

	def test_leaf_to_html_no_tag(self):
		node = LeafNode(None, "Hello, world!")
		self.assertEqual(node.to_html(), "Hello, world!")

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

if __name__ == "__main__":
	unittest.main()
