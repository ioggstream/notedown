import notedown


class TestCommandLine(object):
    @property
    def default_args(self):
        parser = notedown.main.command_line_parser()
        return parser.parse_args()

    def run(self, args):
        notedown.main.main(args)

    def test_basic(self):
        args = self.default_args
        args.input_file = 'example.md'
        self.run(args)

    def test_reverse(self):
        args = self.default_args
        args.input_file = 'example.ipynb'
        self.run(args)

    def test_markdown_to_notebook(self):
        args = self.default_args
        args.input_file = 'example.md'
        args.informat = 'markdown'
        args.outformat = 'notebook'
        self.run(args)

    def test_markdown_to_markdown(self):
        args = self.default_args
        args.input_file = 'example.md'
        args.informat = 'markdown'
        args.outformat = 'markdown'
        self.run(args)

    def test_notebook_to_markdown(self):
        args = self.default_args
        args.input_file = 'example.ipynb'
        args.informat = 'notebook'
        args.outformat = 'markdown'
        self.run(args)

    def test_notebook_to_notebook(self):
        args = self.default_args
        args.input_file = 'example.ipynb'
        args.informat = 'notebook'
        args.outformat = 'notebook'
        self.run(args)
