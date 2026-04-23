 1  namespace Sandbox
 2  
 3  /// represents a validated TREC identifier
 4  type TrecId = private TrecId of string
 5  
 6  module TrecId =
 7  
 8      /// construct a TrecId if the input satisfies domain rules
 9      let create (input : string) =
10          match input with
11          | null -> Error "trec id cannot be null"
12          | s when s.Trim() = "" -> Error "trec id cannot be empty"
13          | s when s.Contains(" ") -> Error "trec id cannot contain whitespace"
14          | s -> Ok (TrecId s)
15  
16      /// unwrap the value object
17      let value (TrecId s) = s
