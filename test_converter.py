import unittest

from KickAssemblerToDoxygen import *

class TestClass(unittest.TestCase):
  def testremoveAssert(self):
    sourceCode = ".assert \"macroName(x)\", { macroName(1) }, { lda #1 }"
    expected = ""
    self.assertEqual(removeAssert(sourceCode), expected, "Should be empty")

  def testremoveAssertWithoutCurlyBraces(self):
    sourceCode = ".assert \"macroName(x)\", macroName(1), 1"
    expected = ""
    self.assertEqual(removeAssert(sourceCode), expected, "Should be empty")

  def testremoveAssertError(self):
    sourceCode = ".asserterror \"macroName(x)\", { macroName(1) }"
    expected = ""
    self.assertEqual(removeAssertError(sourceCode), expected, "Should be empty")

  def testremoveFileNameSpace(self):
    sourceCode = ".filenamespace xyz\n"
    expected = ""
    self.assertEqual(removeFileNameSpace(sourceCode), expected, "Should be empty")

  def testremoveImportDoubleQuote(self):
    sourceCode = "#import \"fileToImport.asm\"\n"
    expected = ""
    self.assertEqual(removeImport(sourceCode), expected, "Should be empty")

  def testremoveImportDoubleQuote(self):
    sourceCode = "#import \"fileToImport.asm\"\n"
    expected = ""
    self.assertEqual(removeImport(sourceCode), expected, "Should be empty")

  def testremoveImportOnce(self):
    sourceCode = "#importonce\n"
    expected = ""
    self.assertEqual(removeImportOnce(sourceCode), expected, "Should be empty")

  def testremoveInitalDotFromKeywordsNamespace(self):
    sourceCode = ".namespace "
    expected = "namespace "
    self.assertEqual(removeInitalDotFromKeywords(sourceCode), expected, "Should not have initial dot")

  def testremoveInitalDotFromKeywordsMacro(self):
    sourceCode = ".macro "
    expected = "macro "
    self.assertEqual(removeInitalDotFromKeywords(sourceCode), expected, "Should not have initial dot")

  def testremoveInitalDotFromKeywordsFunction(self):
    sourceCode = ".function "
    expected = "function "
    self.assertEqual(removeInitalDotFromKeywords(sourceCode), expected, "Should not have initial dot")

  def testremoveInitalDotFromKeywordsLabel(self):
    sourceCode = ".label "
    expected = "label "
    self.assertEqual(removeInitalDotFromKeywords(sourceCode), expected, "Should not have initial dot")

  def testremoveInitalDotFromKeywordsPseudocommand(self):
    sourceCode = ".pseudocommand "
    expected = "pseudocommand "
    self.assertEqual(removeInitalDotFromKeywords(sourceCode), expected, "Should not have initial dot")

  def testAddSemicolonToLabel(self):
    sourceCode = "label xyz = $beef"
    expected = "label xyz = $beef;"
    self.assertEqual(addSemicolorToLabelDeclaration(sourceCode), expected, "Should have semicolon at end")

if __name__=='__main__':
	unittest.main()
