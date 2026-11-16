# Code examples — Rust for Beginners

Every numbered example from the book *Rust for Beginners* by Oscar Gomez, organized by chapter. Example 01 → `example_01.rs`.

## How to use

1. Install Rust with [rustup](https://rustup.rs) (the examples were tested with Rust 1.97, edition 2024).
2. **Single-file examples:** create a project with `cargo new playground`, copy the example into `playground/src/main.rs` and run `cargo run`. Examples without a `main` function (libraries and tests) run with `cargo test`.
3. **Project chapters** (16, 22 and 24-28) contain complete Cargo projects (`guessing_game/`, `unit_converter/`, `todo/`, `seek/`, `library/`, `webserver/`...). Open the folder and run `cargo run` or `cargo test`. The book shows how each file is built step by step.

## License

The code is released under the MIT License (see the LICENSE file in the root of this repository). Third-party libraries, tools and models keep their own licenses.

## List of examples

| # | File | Title |
|---|---|---|
| 01 | `ch01_What_Is_Programming/example_01.rs` | Hello, world! |
| 02 | `ch01_What_Is_Programming/example_02.rs` | Calculating a total price |
| 03 | `ch02_Setting_Up_Your_Rust_Workshop/example_03.rs` | Hello from a single file |
| 04 | `ch02_Setting_Up_Your_Rust_Workshop/example_04.rs` | A personal greeting |
| 05 | `ch02_Setting_Up_Your_Rust_Workshop/example_05.rs` | Two ways to fill placeholders |
| 06 | `ch03_Thinking_Like_a_Programmer/example_06.rs` | Finding the largest number |
| 07 | `ch03_Thinking_Like_a_Programmer/example_07.rs` | Accumulate and count patterns |
| 08 | `ch03_Thinking_Like_a_Programmer/example_08.rs` | From pseudocode to Rust |
| 09 | `ch03_Thinking_Like_a_Programmer/example_09.rs` | Using dbg! to inspect values |
| 10 | `ch03_Thinking_Like_a_Programmer/example_10.rs` | Shop discount calculator |
| 11 | `ch04_Variables_Mutability_and_Data_Types/example_11.rs` | Creating variables with let |
| 12 | `ch04_Variables_Mutability_and_Data_Types/example_12.rs` | Mutable variables with mut |
| 13 | `ch04_Variables_Mutability_and_Data_Types/example_13.rs` | Using constants |
| 14 | `ch04_Variables_Mutability_and_Data_Types/example_14.rs` | Shadowing a variable |
| 15 | `ch04_Variables_Mutability_and_Data_Types/example_15.rs` | Type inference and type annotations |
| 16 | `ch04_Variables_Mutability_and_Data_Types/example_16.rs` | Writing integer literals |
| 17 | `ch04_Variables_Mutability_and_Data_Types/example_17.rs` | Handling overflow explicitly |
| 18 | `ch04_Variables_Mutability_and_Data_Types/example_18.rs` | Floating-point numbers |
| 19 | `ch04_Variables_Mutability_and_Data_Types/example_19.rs` | Booleans |
| 20 | `ch04_Variables_Mutability_and_Data_Types/example_20.rs` | The char type |
| 21 | `ch04_Variables_Mutability_and_Data_Types/example_21.rs` | Tuples |
| 22 | `ch04_Variables_Mutability_and_Data_Types/example_22.rs` | Arrays |
| 23 | `ch04_Variables_Mutability_and_Data_Types/example_23.rs` | Converting with as |
| 24 | `ch04_Variables_Mutability_and_Data_Types/example_24.rs` | A weekly step counter |
| 25 | `ch05_Operators_Expressions_and_Statements/example_25.rs` | Basic arithmetic |
| 26 | `ch05_Operators_Expressions_and_Statements/example_26.rs` | Integer versus floating-point division |
| 27 | `ch05_Operators_Expressions_and_Statements/example_27.rs` | Practical uses of the remainder |
| 28 | `ch05_Operators_Expressions_and_Statements/example_28.rs` | Compound assignment |
| 29 | `ch05_Operators_Expressions_and_Statements/example_29.rs` | Comparing different kinds of values |
| 30 | `ch05_Operators_Expressions_and_Statements/example_30.rs` | Combining conditions |
| 31 | `ch05_Operators_Expressions_and_Statements/example_31.rs` | Precedence and parentheses |
| 32 | `ch05_Operators_Expressions_and_Statements/example_32.rs` | A block is an expression |
| 33 | `ch05_Operators_Expressions_and_Statements/example_33.rs` | Using if as an expression |
| 34 | `ch05_Operators_Expressions_and_Statements/example_34.rs` | Bitwise operators |
| 35 | `ch05_Operators_Expressions_and_Statements/example_35.rs` | Useful number methods |
| 36 | `ch05_Operators_Expressions_and_Statements/example_36.rs` | BMI calculator |
| 37 | `ch06_Control_Flow/example_37.rs` | A grading program |
| 38 | `ch06_Control_Flow/example_38.rs` | Nested if statements |
| 39 | `ch06_Control_Flow/example_39.rs` | A countdown with loop |
| 40 | `ch06_Control_Flow/example_40.rs` | Returning a value from a loop |
| 41 | `ch06_Control_Flow/example_41.rs` | Doubling money with while |
| 42 | `ch06_Control_Flow/example_42.rs` | Looping over an array with for |
| 43 | `ch06_Control_Flow/example_43.rs` | Ranges in for loops |
| 44 | `ch06_Control_Flow/example_44.rs` | Using enumerate |
| 45 | `ch06_Control_Flow/example_45.rs` | Using continue and break |
| 46 | `ch06_Control_Flow/example_46.rs` | Breaking out of nested loops |
| 47 | `ch06_Control_Flow/example_47.rs` | Choosing with match |
| 48 | `ch06_Control_Flow/example_48.rs` | Ranges and guards in match |
| 49 | `ch06_Control_Flow/example_49.rs` | FizzBuzz with match |
| 50 | `ch06_Control_Flow/example_50.rs` | Counting prime numbers |
| 51 | `ch07_Functions_and_Modular_Thinking/example_51.rs` | Defining and calling functions |
| 52 | `ch07_Functions_and_Modular_Thinking/example_52.rs` | Functions with parameters |
| 53 | `ch07_Functions_and_Modular_Thinking/example_53.rs` | A function that returns a value |
| 54 | `ch07_Functions_and_Modular_Thinking/example_54.rs` | Early return |
| 55 | `ch07_Functions_and_Modular_Thinking/example_55.rs` | Returning a tuple |
| 56 | `ch07_Functions_and_Modular_Thinking/example_56.rs` | Watching the call stack |
| 57 | `ch07_Functions_and_Modular_Thinking/example_57.rs` | Recursive factorial |
| 58 | `ch07_Functions_and_Modular_Thinking/example_58.rs` | Before refactoring |
| 59 | `ch07_Functions_and_Modular_Thinking/example_59.rs` | After refactoring |
| 60 | `ch07_Functions_and_Modular_Thinking/example_60.rs` | A grade report built from functions |
| 61 | `ch08_How_Memory_Works/example_61.rs` | Measuring the size of types |
| 62 | `ch08_How_Memory_Works/example_62.rs` | A String grows on the heap |
| 63 | `ch08_How_Memory_Works/example_63.rs` | Watching a String's capacity grow |
| 64 | `ch08_How_Memory_Works/example_64.rs` | Values are dropped at the end of their scope |
| 65 | `ch08_How_Memory_Works/example_65.rs` | Copying stack values |
| 66 | `ch09_Ownership/example_66.rs` | Using the new owner after a move |
| 67 | `ch09_Ownership/example_67.rs` | Cloning a String |
| 68 | `ch09_Ownership/example_68.rs` | Integers are copied, not moved |
| 69 | `ch09_Ownership/example_69.rs` | Passing values to functions |
| 70 | `ch09_Ownership/example_70.rs` | Functions that return ownership |
| 71 | `ch09_Ownership/example_71.rs` | Returning ownership with a tuple |
| 72 | `ch09_Ownership/example_72.rs` | Moving one field out of a tuple |
| 73 | `ch09_Ownership/example_73.rs` | Following ownership through a program |
| 74 | `ch10_Borrowing_and_References/example_74.rs` | Borrowing with a reference |
| 75 | `ch10_Borrowing_and_References/example_75.rs` | Modifying through a mutable reference |
| 76 | `ch10_Borrowing_and_References/example_76.rs` | Many shared references at once |
| 77 | `ch10_Borrowing_and_References/example_77.rs` | Borrows end at their last use |
| 78 | `ch10_Borrowing_and_References/example_78.rs` | Returning an owned value instead |
| 79 | `ch10_Borrowing_and_References/example_79.rs` | Dereferencing with * |
| 80 | `ch10_Borrowing_and_References/example_80.rs` | Looping over references |
| 81 | `ch10_Borrowing_and_References/example_81.rs` | Text statistics with borrowing |
| 82 | `ch11_Strings_and_Slices/example_82.rs` | Array slices |
| 83 | `ch11_Strings_and_Slices/example_83.rs` | Functions that accept slices |
| 84 | `ch11_Strings_and_Slices/example_84.rs` | A mutable slice |
| 85 | `ch11_Strings_and_Slices/example_85.rs` | String literals and String values |
| 86 | `ch11_Strings_and_Slices/example_86.rs` | Prefer &str parameters |
| 87 | `ch11_Strings_and_Slices/example_87.rs` | Bytes versus characters |
| 88 | `ch11_Strings_and_Slices/example_88.rs` | Characters and bytes |
| 89 | `ch11_Strings_and_Slices/example_89.rs` | Slicing a string by bytes |
| 90 | `ch11_Strings_and_Slices/example_90.rs` | Building a String |
| 91 | `ch11_Strings_and_Slices/example_91.rs` | Ways to join text |
| 92 | `ch11_Strings_and_Slices/example_92.rs` | Common text methods |
| 93 | `ch11_Strings_and_Slices/example_93.rs` | Splitting text |
| 94 | `ch11_Strings_and_Slices/example_94.rs` | Parsing numbers from text |
| 95 | `ch11_Strings_and_Slices/example_95.rs` | A word analyzer |
| 96 | `ch12_Structs_and_Methods/example_96.rs` | Defining and using a struct |
| 97 | `ch12_Structs_and_Methods/example_97.rs` | Changing fields of a mutable struct |
| 98 | `ch12_Structs_and_Methods/example_98.rs` | Field init shorthand |
| 99 | `ch12_Structs_and_Methods/example_99.rs` | Struct update syntax |
| 100 | `ch12_Structs_and_Methods/example_100.rs` | Printing a struct with Debug |
| 101 | `ch12_Structs_and_Methods/example_101.rs` | Defining methods with impl |
| 102 | `ch12_Structs_and_Methods/example_102.rs` | The three kinds of self |
| 103 | `ch12_Structs_and_Methods/example_103.rs` | A constructor with new |
| 104 | `ch12_Structs_and_Methods/example_104.rs` | Tuple structs |
| 105 | `ch12_Structs_and_Methods/example_105.rs` | Nested structs |
| 106 | `ch12_Structs_and_Methods/example_106.rs` | A bank account struct |
| 107 | `ch13_Enums_and_Pattern_Matching/example_107.rs` | A simple enum |
| 108 | `ch13_Enums_and_Pattern_Matching/example_108.rs` | Matching on enum variants |
| 109 | `ch13_Enums_and_Pattern_Matching/example_109.rs` | Enum variants with data |
| 110 | `ch13_Enums_and_Pattern_Matching/example_110.rs` | Methods on an enum |
| 111 | `ch13_Enums_and_Pattern_Matching/example_111.rs` | Using Option |
| 112 | `ch13_Enums_and_Pattern_Matching/example_112.rs` | Option in the standard library |
| 113 | `ch13_Enums_and_Pattern_Matching/example_113.rs` | Using if let |
| 114 | `ch13_Enums_and_Pattern_Matching/example_114.rs` | Using let else |
| 115 | `ch13_Enums_and_Pattern_Matching/example_115.rs` | Option methods |
| 116 | `ch13_Enums_and_Pattern_Matching/example_116.rs` | Combining patterns |
| 117 | `ch13_Enums_and_Pattern_Matching/example_117.rs` | A simple state machine |
| 118 | `ch14_Collections_Vec_HashMap_and_HashSet/example_118.rs` | Creating and growing a vector |
| 119 | `ch14_Collections_Vec_HashMap_and_HashSet/example_119.rs` | Indexing versus get |
| 120 | `ch14_Collections_Vec_HashMap_and_HashSet/example_120.rs` | Changing a vector |
| 121 | `ch14_Collections_Vec_HashMap_and_HashSet/example_121.rs` | Three ways to loop over a vector |
| 122 | `ch14_Collections_Vec_HashMap_and_HashSet/example_122.rs` | A vector of structs |
| 123 | `ch14_Collections_Vec_HashMap_and_HashSet/example_123.rs` | Creating and using a HashMap |
| 124 | `ch14_Collections_Vec_HashMap_and_HashSet/example_124.rs` | Iterating in sorted order |
| 125 | `ch14_Collections_Vec_HashMap_and_HashSet/example_125.rs` | Counting words with the entry API |
| 126 | `ch14_Collections_Vec_HashMap_and_HashSet/example_126.rs` | A HashMap owns its keys and values |
| 127 | `ch14_Collections_Vec_HashMap_and_HashSet/example_127.rs` | Using a HashSet |
| 128 | `ch14_Collections_Vec_HashMap_and_HashSet/example_128.rs` | Set operations |
| 129 | `ch14_Collections_Vec_HashMap_and_HashSet/example_129.rs` | A gradebook with HashMap and Vec |
| 130 | `ch15_Error_Handling_Option_Result_and/example_130.rs` | Causing a panic on purpose |
| 131 | `ch15_Error_Handling_Option_Result_and/example_131.rs` | Handling a Result with match |
| 132 | `ch15_Error_Handling_Option_Result_and/example_132.rs` | A function that returns Result |
| 133 | `ch15_Error_Handling_Option_Result_and/example_133.rs` | Propagating errors with ? |
| 134 | `ch15_Error_Handling_Option_Result_and/example_134.rs` | Using ? with Option |
| 135 | `ch15_Error_Handling_Option_Result_and/example_135.rs` | main returning a Result |
| 136 | `ch15_Error_Handling_Option_Result_and/example_136.rs` | Result methods in action |
| 137 | `ch15_Error_Handling_Option_Result_and/example_137.rs` | Reading and writing files |
| 138 | `ch15_Error_Handling_Option_Result_and/example_138.rs` | Reacting to the kind of error |
| 139 | `ch15_Error_Handling_Option_Result_and/example_139.rs` | A custom error enum |
| 140 | `ch15_Error_Handling_Option_Result_and/example_140.rs` | Converting errors with map_err |
| 141 | `ch15_Error_Handling_Option_Result_and/example_141.rs` | A robust order line parser |
| 142 | `ch16_Modules_Packages_and_Crates/example_142.rs` | Modules inside one file |
| 143 | `ch16_Modules_Packages_and_Crates/example_143.rs` | Private fields protect invariants |
| 144 | `ch16_Modules_Packages_and_Crates/example_144.rs` | Bringing names into scope with use |
| 145 | `ch16_Modules_Packages_and_Crates/example_145.rs` | Paths with crate, self and super |
| 146 | `ch16_Modules_Packages_and_Crates/inventory_project/src/main.rs` | Project file: src/main.rs |
| 147 | `ch16_Modules_Packages_and_Crates/inventory_project/src/inventory.rs` | Project file: src/inventory.rs |
| 148 | `ch16_Modules_Packages_and_Crates/inventory_project/src/inventory/item.rs` | Project file: src/inventory/item.rs |
| 149 | `ch16_Modules_Packages_and_Crates/example_149.rs` | Using the rand crate |
| 150 | `ch17_Generics/example_150.rs` | A generic function |
| 151 | `ch17_Generics/example_151.rs` | Returning a reference to the largest item |
| 152 | `ch17_Generics/example_152.rs` | A generic struct |
| 153 | `ch17_Generics/example_153.rs` | A struct with two type parameters |
| 154 | `ch17_Generics/example_154.rs` | A generic enum of your own |
| 155 | `ch17_Generics/example_155.rs` | Methods on a generic struct |
| 156 | `ch17_Generics/example_156.rs` | Using a where clause |
| 157 | `ch17_Generics/example_157.rs` | A generic Stack |
| 158 | `ch18_Traits/example_158.rs` | Defining and implementing a trait |
| 159 | `ch18_Traits/example_159.rs` | Default methods in a trait |
| 160 | `ch18_Traits/example_160.rs` | Accepting any type that implements a trait |
| 161 | `ch18_Traits/example_161.rs` | Returning impl Trait |
| 162 | `ch18_Traits/example_162.rs` | A collection of trait objects |
| 163 | `ch18_Traits/example_163.rs` | Deriving standard traits |
| 164 | `ch18_Traits/example_164.rs` | Implementing Display |
| 165 | `ch18_Traits/example_165.rs` | Implementing From |
| 166 | `ch18_Traits/example_166.rs` | Overloading the + operator |
| 167 | `ch18_Traits/example_167.rs` | A notification system with traits |
| 168 | `ch19_Lifetimes_Demystified/example_168.rs` | The longest function with a lifetime |
| 169 | `ch19_Lifetimes_Demystified/example_169.rs` | Only the related parameter needs the lifetime |
| 170 | `ch19_Lifetimes_Demystified/example_170.rs` | A struct that holds a reference |
| 171 | `ch19_Lifetimes_Demystified/example_171.rs` | The 'static lifetime |
| 172 | `ch19_Lifetimes_Demystified/example_172.rs` | A zero-copy configuration parser |
| 173 | `ch20_Closures_and_Iterators/example_173.rs` | Basic closures |
| 174 | `ch20_Closures_and_Iterators/example_174.rs` | A closure captures variables |
| 175 | `ch20_Closures_and_Iterators/example_175.rs` | Capturing by mutable reference |
| 176 | `ch20_Closures_and_Iterators/example_176.rs` | Returning a move closure |
| 177 | `ch20_Closures_and_Iterators/example_177.rs` | Accepting closures as parameters |
| 178 | `ch20_Closures_and_Iterators/example_178.rs` | Calling next by hand |
| 179 | `ch20_Closures_and_Iterators/example_179.rs` | map, filter and collect |
| 180 | `ch20_Closures_and_Iterators/example_180.rs` | Iterators are lazy |
| 181 | `ch20_Closures_and_Iterators/example_181.rs` | More adapters in action |
| 182 | `ch20_Closures_and_Iterators/example_182.rs` | Consumers in action |
| 183 | `ch20_Closures_and_Iterators/example_183.rs` | Collecting into different types |
| 184 | `ch20_Closures_and_Iterators/example_184.rs` | A custom iterator |
| 185 | `ch20_Closures_and_Iterators/example_185.rs` | Analyzing sales with iterators |
| 186 | `ch21_Smart_Pointers_Box_Rc_and_RefCell/example_186.rs` | Creating a Box |
| 187 | `ch21_Smart_Pointers_Box_Rc_and_RefCell/example_187.rs` | A linked list with Box |
| 188 | `ch21_Smart_Pointers_Box_Rc_and_RefCell/example_188.rs` | A binary search tree with Box |
| 189 | `ch21_Smart_Pointers_Box_Rc_and_RefCell/example_189.rs` | Shared ownership with Rc |
| 190 | `ch21_Smart_Pointers_Box_Rc_and_RefCell/example_190.rs` | Interior mutability with RefCell |
| 191 | `ch21_Smart_Pointers_Box_Rc_and_RefCell/example_191.rs` | A RefCell panics when borrowing rules are broken |
| 192 | `ch21_Smart_Pointers_Box_Rc_and_RefCell/example_192.rs` | Shared, mutable data with Rc<RefCell<T>> |
| 193 | `ch21_Smart_Pointers_Box_Rc_and_RefCell/example_193.rs` | Parent and child with Rc and Weak |
| 194 | `ch22_Testing_and_Documentation/example_194.rs` | Unit tests in a library |
| 195 | `ch22_Testing_and_Documentation/example_195.rs` | Assertions with custom messages |
| 196 | `ch22_Testing_and_Documentation/example_196.rs` | Testing that code panics |
| 197 | `ch22_Testing_and_Documentation/example_197.rs` | Tests that return Result |
| 198 | `ch22_Testing_and_Documentation/shipping/tests/pricing.rs` | Project file: tests/pricing.rs |
| 199 | `ch22_Testing_and_Documentation/shipping/src/lib.rs` | Documenting a function |
| 200 | `ch22_Testing_and_Documentation/example_200.rs` | A documented and tested module |
| 201 | `ch23_Fearless_Concurrency/example_201.rs` | Spawning threads |
| 202 | `ch23_Fearless_Concurrency/example_202.rs` | Getting results from threads |
| 203 | `ch23_Fearless_Concurrency/example_203.rs` | Sending messages through a channel |
| 204 | `ch23_Fearless_Concurrency/example_204.rs` | Multiple producers |
| 205 | `ch23_Fearless_Concurrency/example_205.rs` | A Mutex in a single thread |
| 206 | `ch23_Fearless_Concurrency/example_206.rs` | A shared counter with Arc and Mutex |
| 207 | `ch23_Fearless_Concurrency/example_207.rs` | Scoped threads borrowing local data |
| 208 | `ch23_Fearless_Concurrency/example_208.rs` | A parallel word counter |
| 209 | `ch24_Project_1_Guessing_Game_and_Unit_Converter/example_209.rs` | Reading a line from the keyboard |
| 210 | `ch24_Project_1_Guessing_Game_and_Unit_Converter/example_210.rs` | Comparing one guess |
| 211 | `ch24_Project_1_Guessing_Game_and_Unit_Converter/example_211.rs` | Looping until the right guess |
| 212 | `ch24_Project_1_Guessing_Game_and_Unit_Converter/guessing_game/Cargo.toml` | Project file: Cargo.toml |
| 213 | `ch24_Project_1_Guessing_Game_and_Unit_Converter/guessing_game/src/main.rs` | Project file: src/main.rs |
| 214 | `ch24_Project_1_Guessing_Game_and_Unit_Converter/example_214.rs` | Reading command-line arguments |
| 215 | `ch24_Project_1_Guessing_Game_and_Unit_Converter/unit_converter/src/main.rs` | Project file: src/main.rs |
| 216 | `ch25_Project_2_A_ToDo_Manager_with_File_Storage/todo/Cargo.toml` | Project file: Cargo.toml |
| 217 | `ch25_Project_2_A_ToDo_Manager_with_File_Storage/example_217.rs` | A first serde round trip |
| 218 | `ch25_Project_2_A_ToDo_Manager_with_File_Storage/todo/src/task.rs` | Project file: src/task.rs |
| 219 | `ch25_Project_2_A_ToDo_Manager_with_File_Storage/todo/src/storage.rs` | Project file: src/storage.rs |
| 220 | `ch25_Project_2_A_ToDo_Manager_with_File_Storage/todo/src/main.rs` | Project file: src/main.rs |
| 221 | `ch26_Project_3_A_Text_Search_Tool/seek/Cargo.toml` | Project file: Cargo.toml |
| 222 | `ch26_Project_3_A_Text_Search_Tool/seek/src/lib.rs` | Project file: src/lib.rs |
| 223 | `ch26_Project_3_A_Text_Search_Tool/seek/src/main.rs` | Project file: src/main.rs |
| 224 | `ch27_Project_4_A_Library_Management_System/library/Cargo.toml` | Project file: Cargo.toml |
| 225 | `ch27_Project_4_A_Library_Management_System/library/src/items.rs` | Project file: src/items.rs |
| 226 | `ch27_Project_4_A_Library_Management_System/library/src/library.rs` | Project file: src/library.rs |
| 227 | `ch27_Project_4_A_Library_Management_System/library/src/main.rs` | Project file: src/main.rs |
| 228 | `ch27_Project_4_A_Library_Management_System/library/src/library_tests.rs` | Project file: src/library_tests.rs |
| 229 | `ch28_Project_5_A_Multithreaded_Web_Server/webserver/Cargo.toml` | Project file: Cargo.toml |
| 230 | `ch28_Project_5_A_Multithreaded_Web_Server/example_230.rs` | A first TCP listener |
| 231 | `ch28_Project_5_A_Multithreaded_Web_Server/webserver/src/http.rs` | Project file: src/http.rs |
| 232 | `ch28_Project_5_A_Multithreaded_Web_Server/webserver/src/routes.rs` | Project file: src/routes.rs |
| 233 | `ch28_Project_5_A_Multithreaded_Web_Server/webserver/src/main_single.rs` | Single-threaded version of main |
| 234 | `ch28_Project_5_A_Multithreaded_Web_Server/webserver/src/pool.rs` | Project file: src/pool.rs |
| 235 | `ch28_Project_5_A_Multithreaded_Web_Server/webserver/src/main.rs` | Project file: src/main.rs |
| 236 | `ch29_Where_to_Go_Next/example_236.rs` | A simple declarative macro |
| 237 | `appendix_E_Solutions_to_Selected_Exercises/example_237.rs` | Smallest number |
| 238 | `appendix_E_Solutions_to_Selected_Exercises/example_238.rs` | Two discount levels |
| 239 | `appendix_E_Solutions_to_Selected_Exercises/example_239.rs` | Celsius to Fahrenheit |
| 240 | `appendix_E_Solutions_to_Selected_Exercises/example_240.rs` | Seconds to hours, minutes and seconds |
| 241 | `appendix_E_Solutions_to_Selected_Exercises/example_241.rs` | Leap years |
| 242 | `appendix_E_Solutions_to_Selected_Exercises/example_242.rs` | A triangle of stars |
| 243 | `appendix_E_Solutions_to_Selected_Exercises/example_243.rs` | First number divisible by 6 and 8 |
| 244 | `appendix_E_Solutions_to_Selected_Exercises/example_244.rs` | Max of three and recursive sum |
| 245 | `appendix_E_Solutions_to_Selected_Exercises/example_245.rs` | Taking and returning ownership |
| 246 | `appendix_E_Solutions_to_Selected_Exercises/example_246.rs` | Mutable references |
| 247 | `appendix_E_Solutions_to_Selected_Exercises/example_247.rs` | Text utilities |
| 248 | `appendix_E_Solutions_to_Selected_Exercises/example_248.rs` | Splitting key-value pairs |
| 249 | `appendix_E_Solutions_to_Selected_Exercises/example_249.rs` | Rectangle methods |
| 250 | `appendix_E_Solutions_to_Selected_Exercises/example_250.rs` | Division with Option |
| 251 | `appendix_E_Solutions_to_Selected_Exercises/example_251.rs` | Parsing commands into an enum |
| 252 | `appendix_E_Solutions_to_Selected_Exercises/example_252.rs` | Counting and grouping |
| 253 | `appendix_E_Solutions_to_Selected_Exercises/example_253.rs` | Parsing a point with ? and map_err |
| 254 | `appendix_E_Solutions_to_Selected_Exercises/example_254.rs` | Generic helpers |
| 255 | `appendix_E_Solutions_to_Selected_Exercises/example_255.rs` | Display and From |
| 256 | `appendix_E_Solutions_to_Selected_Exercises/example_256.rs` | Iterators and closures |
| 257 | `appendix_E_Solutions_to_Selected_Exercises/example_257.rs` | A Countdown iterator |
| 258 | `appendix_E_Solutions_to_Selected_Exercises/example_258.rs` | A counter with RefCell |
| 259 | `appendix_E_Solutions_to_Selected_Exercises/example_259.rs` | Tests for leap years and division |
| 260 | `appendix_E_Solutions_to_Selected_Exercises/example_260.rs` | Channels and a shared log |
| 261 | `appendix_E_Solutions_to_Selected_Exercises/example_261.rs` | Average of numbers typed by the user |
