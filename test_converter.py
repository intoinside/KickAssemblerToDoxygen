import unittest

from KickAssemblerToDoxygen import *

class TestClass(unittest.TestCase):
  def testremoveAssert(self):
    sourceCode = ".assert \"macroName()\", { macroName() }, { lda #1; bpl *+5; jmp $0000 }"
    expected = ""
    self.assertEqual(remove_assert(sourceCode), expected, "Should be empty")

  def testremoveAssert2(self):
    sourceCode = ".assert \"macroName(x)\", { macroName(1) }, { lda #1; bpl *+5; jmp $0000 }"
    expected = ""
    self.assertEqual(remove_assert(sourceCode), expected, "Should be empty")

  def testremoveAssert3(self):
    sourceCode = ".assert \"macroName(x, y)\", { macroName(1, 2) }, { lda #1; bpl *+5; jmp $0000 }"
    expected = ""
    self.assertEqual(remove_assert(sourceCode), expected, "Should be empty")

  def testremoveAssert4(self):
    sourceCode = ".assert \"SetSpriteXPosition stores X in SPRITE_X reg\", { SetSpriteXPosition(3, 5) }, {\n  lda #$05\n  sta $d006\n}"
    expected = ""
    self.assertEqual(remove_assert(sourceCode), expected, "Should be empty")

  def testremoveAssert5(self):
    sourceCode = ".assert \"macroName(x, y)\", macroName(1, 2), lda #0\n"
    expected = ""
    self.assertEqual(remove_assert(sourceCode), expected, "Should be empty")

  def testremoveAssertError(self):
    sourceCode = ".asserterror \"macroName()\", { macroName() }"
    expected = ""
    self.assertEqual(remove_assert_error(sourceCode), expected, "Should be empty")

  def testremoveAssertError2(self):
    sourceCode = ".asserterror \"macroName(10)\", { macroName(10) }"
    expected = ""
    self.assertEqual(remove_assert_error(sourceCode), expected, "Should be empty")

  def testremoveAssertError3(self):
    sourceCode = ".asserterror \"macroName(20, 10)\", { macroName(20, 10) }"
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

  def testremoveInitalDotFromKeywordsConst(self):
    sourceCode = ".const "
    expected = "const "
    self.assertEqual(remove_inital_dot_from_keywords(sourceCode), expected, "Should not have initial dot")

  def testremoveInitalDotFromKeywordsPseudocommand(self):
    sourceCode = ".pseudocommand "
    expected = "pseudocommand "
    self.assertEqual(remove_inital_dot_from_keywords(sourceCode), expected, "Should not have initial dot")

  def testAddSemicolonToLabel(self):
    sourceCode = "label xyz = $beef"
    expected = "label xyz = $beef;"
    self.assertEqual(add_semicolon_to_label_declaration(sourceCode), expected, "Should have semicolon at end")

  def testAddSemicolonToConst(self):
    sourceCode = "const xyz = $beef"
    expected = "const xyz = $beef;"
    self.assertEqual(add_semicolon_to_const_declaration(sourceCode), expected, "Should have semicolon at end")

  def testRemoveSomeNewLine(self):
    sourceCode = "\n\n\n/**"
    expected = "\n\n/**"
    self.assertEqual(remove_some_newline(sourceCode), expected, "Should have reduced newline")

  def testRemoveSomeNewLine2(self):
    sourceCode = "\n\n\n\n/**"
    expected = "\n\n/**"
    self.assertEqual(remove_some_newline(sourceCode), expected, "Should have reduced newline")

  def testRemoveSomeNewLine2(self):
    sourceCode = "\n/**"
    expected = "\n/**"
    self.assertEqual(remove_some_newline(sourceCode), expected, "Should have not reduced newline")

  def testFixStruct(self):
    sourceCode = ".struct name {value, value2}"
    expected = ".struct name {value, value2,};"
    self.assertEqual(fix_struct_definition(sourceCode), expected, "Should have fixed struct")

#   def testReplaceBodyInCurlyBrackets(self):
#     sourceCode = """.macro SetVICBank(bank) {
# lda Cia.CIA2_DATA_PORT_A
# and #%11111100
# ora #[bank & %00000011]
# sta Cia.CIA2_DATA_PORT_A
# }"""
#     expected = ".macro SetVICBank(bank) ;"
#     self.assertEqual(replace_body_in_curly_brackets(sourceCode), expected, "Should leave only macro definition")

#   def testReplaceBodyInCurlyBracketsWithMultiBrackets(self):
#     sourceCode = """.macro SetBankConfiguration(id) {
#     .if(id==0) {
#       lda #%00111111   // no roms, RAM 0
#     }
#     .if(id==1) {
#       lda #%01111111   // no roms, RAM 1
#     }
#     .if(id==12) {
#       lda #%00000110   // internal function ROM, Kernal and IO, RAM 0
#     }
#     .if(id==14) {
#       lda #%00000001   // all roms, char ROM, RAM 0
#     }
#     .if(id==15) {
#       lda #%00000000  // all roms, RAM 0. default setting.
#     }
#     .if(id==99) {
#       lda #%00001110  // IO, kernal, RAM0. No basic,48K RAM.
#     }
#     sta Mmu.LOAD_CONFIGURATION
# }"""
#     expected = ".macro SetBankConfiguration(id) ;"
#     self.assertEqual(replace_body_in_curly_brackets(sourceCode), expected, "Should leave only macro definition")

  def testFullFile(self):
    sourceCode = """/**
  @file vdc.asm
  @brief Vdc module

  @copyright MIT Licensed
  @date 2022
*/
#importonce

.filenamespace c128lib

.namespace Vdc {
  
/** Vdc color black */
.label VDC_BLACK = 0
/** Vdc color dark gray */
.label VDC_DARK_GRAY = 1
/** Vdc color dark blue */
.label VDC_DARK_BLUE = 2

}

/**
  Sets X position of given sprite (uses sprite MSB register if necessary)

  @param[in] spriteNo Number of the sprite to move
  @param[in] x X position of sprite

  @note Use c128lib_SetSpriteXPosition in sprites-global.asm

  @remark Register .A will be modified.
  Flags N and Z will be affected.

  @since 0.6.0
*/
.macro SetSpriteXPosition(spriteNo, x) {
  .errorif (spriteNo < 0 || spriteNo > 7), "spriteNo must be from 0 to 7"
  .if (x > 255) {
    lda #<x
    sta spriteXReg(spriteNo)
    lda Vic2.SPRITE_MSB_X
    ora #spriteMask(spriteNo)
    sta Vic2.SPRITE_MSB_X
  } else {
    lda #x
    sta spriteXReg(spriteNo)
  }
}
.asserterror "SetSpriteXPosition(-1, 10)", { SetSpriteXPosition(-1, 10) }
.asserterror "SetSpriteXPosition(8, 10)", { SetSpriteXPosition(8, 10) }
.assert "SetSpriteXPosition stores X in SPRITE_X reg", { SetSpriteXPosition(3, 5) }, {
  lda #$05
  sta $d006
}
.assert "SetSpriteXPosition stores X in SPRITE_X and MSB regs", { SetSpriteXPosition(3, 257) },  {
  lda #$01
  sta $d006
  lda $d010
  ora #%00001000
  sta $d010
}
"""
    expected = """/**
  @file vdc.asm
  @brief Vdc module

  @copyright MIT Licensed
  @date 2022
*/


namespace Vdc {
  
/** Vdc color black */
label VDC_BLACK = 0;
/** Vdc color dark gray */
label VDC_DARK_GRAY = 1;
/** Vdc color dark blue */
label VDC_DARK_BLUE = 2;

}

/**
  Sets X position of given sprite (uses sprite MSB register if necessary)

  @param[in] spriteNo Number of the sprite to move
  @param[in] x X position of sprite

  @note Use c128lib_SetSpriteXPosition in sprites-global.asm

  @remark Register .A will be modified.
  Flags N and Z will be affected.

  @since 0.6.0
*/
macro SetSpriteXPosition(spriteNo, x) {
  .errorif (spriteNo < 0 || spriteNo > 7), "spriteNo must be from 0 to 7"
  .if (x > 255) {
    lda #<x
    sta spriteXReg(spriteNo)
    lda Vic2.SPRITE_MSB_X
    ora #spriteMask(spriteNo)
    sta Vic2.SPRITE_MSB_X
  } else {
    lda #x
    sta spriteXReg(spriteNo)
  }
}




"""
    self.assertEqual(convert_file(sourceCode), expected, "Should clean everything")

  def testUsage(self):
    try:
      usage()
    except Exception as exc:
      assert False, f"'Usage' raised an exception {exc}"
      
if __name__=='__main__':
	unittest.main()
