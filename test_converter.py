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
    sourceCode = ".assert \"macroName(x, y)\", macroName(1, 2), $0000\n"
    expected = "\n"
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

  def testremoveInitalDotFromKeywordsPseudocommand(self):
    sourceCode = ".pseudocommand "
    expected = "pseudocommand "
    self.assertEqual(remove_inital_dot_from_keywords(sourceCode), expected, "Should not have initial dot")

  def testAddSemicolonToLabel(self):
    sourceCode = "label xyz = $beef"
    expected = "label xyz = $beef;"
    self.assertEqual(add_semicolor_to_label_declaration(sourceCode), expected, "Should have semicolon at end")

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

  def testReplaceBodyInCurlyBrackets(self):
    sourceCode = """.macro SetVICBank(bank) {
lda Cia.CIA2_DATA_PORT_A
and #%11111100
ora #[bank & %00000011]
sta Cia.CIA2_DATA_PORT_A
}"""
    expected = ".macro SetVICBank(bank) ;"
    self.assertEqual(replace_body_in_curly_brackets(sourceCode), expected, "Should leave only macro definition")

  def testReplaceBodyInCurlyBracketsWithMultiBrackets(self):
    sourceCode = """.macro SetBankConfiguration(id) {
    .if(id==0) {
      lda #%00111111   // no roms, RAM 0
    }
    .if(id==1) {
      lda #%01111111   // no roms, RAM 1
    }
    .if(id==12) {
      lda #%00000110   // internal function ROM, Kernal and IO, RAM 0
    }
    .if(id==14) {
      lda #%00000001   // all roms, char ROM, RAM 0
    }
    .if(id==15) {
      lda #%00000000  // all roms, RAM 0. default setting.
    }
    .if(id==99) {
      lda #%00001110  // IO, kernal, RAM0. No basic,48K RAM.
    }
    sta Mmu.LOAD_CONFIGURATION
}"""
    expected = ".macro SetBankConfiguration(id) ;"
    self.assertEqual(replace_body_in_curly_brackets(sourceCode), expected, "Should leave only macro definition")

  def testFullFile(self):
    sourceCode = """/*
 * c128lib - 8502
 *
 * References available at
 * https://www.cubic.org/~doj/c64/mapping128.pdf
 */
#importonce

.filenamespace c128lib

.namespace Mos8502 {
  
/*
  MOS8502 Registers
*/
.label MOS_8502_DIRECTION       = $00
.label MOS_8502_IO              = $01

/*
  I/O Register bits.
*/
.label CASETTE_MOTOR_OFF        = %00100000
.label CASETTE_SWITCH_CLOSED    = %00010000
.label CASETTE_DATA             = %00001000
.label PLA_CHAREN               = %00000100
.label PLA_HIRAM                = %00000010
.label PLA_LORAM                = %00000001

/*
  Possible I/O & PLA configurations.
*/
.label RAM_RAM_RAM              = %000
.label RAM_CHAR_RAM             = PLA_LORAM
.label RAM_CHAR_KERNAL          = PLA_HIRAM
.label BASIC_CHAR_KERNAL        = PLA_LORAM | PLA_HIRAM
.label RAM_IO_RAM               = PLA_CHAREN | PLA_LORAM
.label RAM_IO_KERNAL            = PLA_CHAREN | PLA_HIRAM
.label BASIC_IO_KERNAL          = PLA_CHAREN | PLA_LORAM | PLA_HIRAM

}

.macro configureMemory(config) {
    lda Mos8502.MOS_8502_IO
    and #%11111000
    ora #[config & %00000111]
    sta Mos8502.MOS_8502_IO
}

/*
  Disable NMI by pointing NMI vector to rti
*/
.macro disableNMI() {
    lda #<nmi
    sta c128lib.NMI_LO
    lda #>nmi
    sta c128lib.NMI_HI
    jmp end
  nmi: 
    rti
  end:
}
"""
    expected = """/*
 * c128lib - 8502
 *
 * References available at
 * https://www.cubic.org/~doj/c64/mapping128.pdf
 */


namespace Mos8502 {
  
/*
  MOS8502 Registers
*/
label MOS_8502_DIRECTION       = $00;
label MOS_8502_IO              = $01;

/*
  I/O Register bits.
*/
label CASETTE_MOTOR_OFF        = %00100000;
label CASETTE_SWITCH_CLOSED    = %00010000;
label CASETTE_DATA             = %00001000;
label PLA_CHAREN               = %00000100;
label PLA_HIRAM                = %00000010;
label PLA_LORAM                = %00000001;

/*
  Possible I/O & PLA configurations.
*/
label RAM_RAM_RAM              = %000;
label RAM_CHAR_RAM             = PLA_LORAM;
label RAM_CHAR_KERNAL          = PLA_HIRAM;
label BASIC_CHAR_KERNAL        = PLA_LORAM | PLA_HIRAM;
label RAM_IO_RAM               = PLA_CHAREN | PLA_LORAM;
label RAM_IO_KERNAL            = PLA_CHAREN | PLA_HIRAM;
label BASIC_IO_KERNAL          = PLA_CHAREN | PLA_LORAM | PLA_HIRAM;

}

macro configureMemory(config) ;

/*
  Disable NMI by pointing NMI vector to rti
*/
macro disableNMI() ;
"""
    self.assertEqual(convert_file(sourceCode), expected, "Should clean everything")

  def testFullFileWithoutNamespace(self):
    sourceCode = """/*
 * c128lib - 8502
 *
 * References available at
 * https://www.cubic.org/~doj/c64/mapping128.pdf
 */
#importonce

.filenamespace c128lib

/*
  MOS8502 Registers
*/
.label MOS_8502_DIRECTION       = $00
.label MOS_8502_IO              = $01

/*
  I/O Register bits.
*/
.label CASETTE_MOTOR_OFF        = %00100000
.label CASETTE_SWITCH_CLOSED    = %00010000
.label CASETTE_DATA             = %00001000
.label PLA_CHAREN               = %00000100
.label PLA_HIRAM                = %00000010
.label PLA_LORAM                = %00000001

/*
  Possible I/O & PLA configurations.
*/
.label RAM_RAM_RAM              = %000
.label RAM_CHAR_RAM             = PLA_LORAM
.label RAM_CHAR_KERNAL          = PLA_HIRAM
.label BASIC_CHAR_KERNAL        = PLA_LORAM | PLA_HIRAM
.label RAM_IO_RAM               = PLA_CHAREN | PLA_LORAM
.label RAM_IO_KERNAL            = PLA_CHAREN | PLA_HIRAM
.label BASIC_IO_KERNAL          = PLA_CHAREN | PLA_LORAM | PLA_HIRAM

.macro configureMemory(config) {
    lda Mos8502.MOS_8502_IO
    and #%11111000
    ora #[config & %00000111]
    sta Mos8502.MOS_8502_IO
}

/*
  Disable NMI by pointing NMI vector to rti
*/
.macro disableNMI() {
    lda #<nmi
    sta c128lib.NMI_LO
    lda #>nmi
    sta c128lib.NMI_HI
    jmp end
  nmi: 
    rti
  end:
}
"""
    expected = """/*
 * c128lib - 8502
 *
 * References available at
 * https://www.cubic.org/~doj/c64/mapping128.pdf
 */


/*
  MOS8502 Registers
*/
label MOS_8502_DIRECTION       = $00;
label MOS_8502_IO              = $01;

/*
  I/O Register bits.
*/
label CASETTE_MOTOR_OFF        = %00100000;
label CASETTE_SWITCH_CLOSED    = %00010000;
label CASETTE_DATA             = %00001000;
label PLA_CHAREN               = %00000100;
label PLA_HIRAM                = %00000010;
label PLA_LORAM                = %00000001;

/*
  Possible I/O & PLA configurations.
*/
label RAM_RAM_RAM              = %000;
label RAM_CHAR_RAM             = PLA_LORAM;
label RAM_CHAR_KERNAL          = PLA_HIRAM;
label BASIC_CHAR_KERNAL        = PLA_LORAM | PLA_HIRAM;
label RAM_IO_RAM               = PLA_CHAREN | PLA_LORAM;
label RAM_IO_KERNAL            = PLA_CHAREN | PLA_HIRAM;
label BASIC_IO_KERNAL          = PLA_CHAREN | PLA_LORAM | PLA_HIRAM;

macro configureMemory(config) ;

/*
  Disable NMI by pointing NMI vector to rti
*/
macro disableNMI() ;
"""
    self.assertEqual(convert_file(sourceCode), expected, "Should clean everything")

  def testUsage(self):
    try:
      usage()
    except Exception as exc:
      assert False, f"'Usage' raised an exception {exc}"
      
if __name__=='__main__':
	unittest.main()
