import unittest

from KickAssemblerToDoxygen import *

class TestClass(unittest.TestCase):
  def testremoveAssert(self):
    sourceCode = ".assert \"macroName(x)\", { macroName(1) }, { lda #1 }"
    expected = ""
    self.assertEqual(remove_assert(sourceCode), expected, "Should be empty")

  def testremoveAssertWithoutCurlyBraces(self):
    sourceCode = ".assert \"macroName(x)\", macroName(1), 1"
    expected = ""
    self.assertEqual(remove_assert(sourceCode), expected, "Should be empty")

  def testremoveAssertError(self):
    sourceCode = ".asserterror \"macroName(x)\", { macroName(1) }"
    expected = ""
    self.assertEqual(remove_assert_error(sourceCode), expected, "Should be empty")

  def testremoveFileNameSpace(self):
    sourceCode = ".filenamespace xyz\n"
    expected = ""
    self.assertEqual(remove_filenamespace(sourceCode), expected, "Should be empty")

  def testremoveImportDoubleQuote(self):
    sourceCode = "#import \"fileToImport.asm\"\n"
    expected = ""
    self.assertEqual(remove_import(sourceCode), expected, "Should be empty")

  def testremoveImportDoubleQuote(self):
    sourceCode = "#import \"fileToImport.asm\"\n"
    expected = ""
    self.assertEqual(remove_import(sourceCode), expected, "Should be empty")

  def testremoveImportOnce(self):
    sourceCode = "#importonce\n"
    expected = ""
    self.assertEqual(remove_importonce(sourceCode), expected, "Should be empty")

  def testremoveInitalDotFromKeywordsNamespace(self):
    sourceCode = ".namespace "
    expected = "namespace "
    self.assertEqual(remove_inital_dot_from_keywords(sourceCode), expected, "Should not have initial dot")

  def testremoveInitalDotFromKeywordsMacro(self):
    sourceCode = ".macro "
    expected = "macro "
    self.assertEqual(remove_inital_dot_from_keywords(sourceCode), expected, "Should not have initial dot")

  def testremoveInitalDotFromKeywordsFunction(self):
    sourceCode = ".function "
    expected = "function "
    self.assertEqual(remove_inital_dot_from_keywords(sourceCode), expected, "Should not have initial dot")

  def testremoveInitalDotFromKeywordsLabel(self):
    sourceCode = ".label "
    expected = "label "
    self.assertEqual(remove_inital_dot_from_keywords(sourceCode), expected, "Should not have initial dot")

  def testremoveInitalDotFromKeywordsPseudocommand(self):
    sourceCode = ".pseudocommand "
    expected = "pseudocommand "
    self.assertEqual(remove_inital_dot_from_keywords(sourceCode), expected, "Should not have initial dot")

  def testAddSemicolonToLabel(self):
    sourceCode = "label xyz = $beef"
    expected = "label xyz = $beef;"
    self.assertEqual(add_semicolor_to_label_declaration(sourceCode), expected, "Should have semicolon at end")

  def testUsage(self):
    try:
      usage()
    except Exception as exc:
      assert False, f"'Usage' raised an exception {exc}"
      
if __name__=='__main__':
	unittest.main()
