import System.Environment
import System.IO
import Data.Char
import Data.List

getSum1 :: [Int] -> Int -> Int
getSum1 [] fst      = 0
getSum1 [x] fst     = if x == fst then x else 0
getSum1 (x:xs) fst  = if x == (head xs) then (x + getSum1 xs fst)
                    else getSum1 xs fst

half :: [Int] -> Int -> Int
half [] _ = 0
half [x] _ = x
half xs i = xs!!((i+((length xs) `quot` 2)) `mod` (length xs))

getSum2 :: [Int] -> [Int] -> Int -> Int
getSum2 [] _ _      = 0
getSum2 [x] ds i    = if x == (half ds i) then x else 0
getSum2 (x:xs) ds i = if x == (half ds i) then (x + getSum2 xs ds (i+1))
                        else getSum2 xs ds (i+1)

main :: IO()
main = do
    argv <- getArgs
    file <- openFile (head argv) ReadMode
    contents <- hGetContents file
    let ds = map digitToInt (init contents)
    putStrLn $ show $ getSum1 ds (head ds)
    putStrLn $ show $ getSum2 ds ds 0
