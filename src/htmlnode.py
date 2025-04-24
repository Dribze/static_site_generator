class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError()

	def props_to_html(self):
		string = ""
		if self.props is None or len(self.props) == 0:
			return string
		for item in self.props:
			string += f' {item}="{self.props[item]}"'
		return string

	def __repr__(self):
		return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value is None:
			raise ValueError("leafNodes must have value")
		if self.tag is None:
			return self.value
		return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

	def __repr__(self):
		return f"LeafNode({self.tag}, {self.value}, {self.props})"
class ParentNode(HTMLNode):
	def __init__(self,tag, children, props=None):
		super().__init__(tag, None, children, props)

	def to_html(self):
		if self.tag is None:
			raise ValueError("must have a tag")
		if self.children is None:
			raise ValueError("must have children")
		string = f'<{self.tag}>'
		for child in self.children:
			string += child.to_html()
		string += f'</{self.tag}>'
		return string
