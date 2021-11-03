from robot.api.parsing import (
    get_model, Documentation, EmptyLine, KeywordCall,
    ModelTransformer, SettingSection, SectionHeader, Token,Documentation,Tags,DefaultTags,ForceTags,
    Setup,SuiteSetup,TestSetup,EmptyLine,Teardown
)

# Awase Khirni Syed awase008@gmail.com

class CaseModifier(ModelTransformer):

    def visit_TestCase(self, node):
        # The matched `TestCase` node is a block with `header` and
        # `body` attributes. `header` is a statement with familiar
        # `get_token` and `get_value` methods for getting certain
        # tokens or their value.
        name = node.header.get_value(Token.TESTCASE_NAME)
        # Returning `None` drops the node altogether i.e. removes
        # this test.
        for i,tcase in enumerate(lists):
            if name == 'loginTest':
                node.body.append(Documentation.from_params("This is my documentations to be added dynamically"))
                node.body.append(Tags.from_params("Mydynamic Tag goes here"))
                node.body.append(Setup.from_params("Mydynamic setup goes here"))
                new_keyword = KeywordCall([
                    Token(Token.SEPARATOR, '    '),
                    Token(Token.KEYWORD, 'New Keyword'),
                    Token(Token.SEPARATOR, '    '),
                    Token(Token.ARGUMENT, 'xxx'),
                    Token(Token.EOL)
                ])
                node.body.append(new_keyword)
                node.body.append(Teardown.from_params("Mydynamic teardown"))
                node.body.append(EmptyLine.from_params())

                #node.body.insert(i, new_keyword)

            return node


        # Construct new keyword call statement from tokens. See `visit_File`
        # below for an example creating statements using `from_params`.

        # Add the keyword call to test as the second item.

        # No need to call `generic_visit` because we are not
        # modifying child nodes. The node itself must to be
        # returned to avoid dropping it.
        return node

    def visit_File(self, node):

        #Removing the old settings
        #node.sections.pop(0)
        # Create settings section with documentation. Needed header and body
        # statements are created using `from_params` method. This is typically
        # more convenient than creating statements based on tokens like above.
        settings = SettingSection(
            header=SectionHeader.from_params(Token.SETTING_HEADER),
            body=[
                Documentation.from_params('This is a really\npowerful API!'),
                EmptyLine.from_params()
            ]
        )
        # Add settings to the beginning of the file.
        node.sections.insert(0, settings)

        # vset=SettingSection(header=SectionHeader.from_params(Token.VARIABLE_HEADER),body="Variables")
        # node.sections.insert(1,vset)
        #tset = SettingSection(header=SectionHeader.from_params(Token.TESTCASE_HEADER), body="Variables")
        # node.sections.insert(2,tset)
        #keyset=SettingSection(header=SectionHeader.from_params(Token.KEYWORD_HEADER),body='Keywords')
        #node.sections.insert(3,keyset)

        # Call `generic_visit` to visit also child nodes.
        return self.generic_visit(node)


    def visit_Tag(self,node):
            node.body.insert(0,'smoketest')
            return node


model = get_model('example.robot')
TestModifier().visit(model)
model.save('modified.robot')
