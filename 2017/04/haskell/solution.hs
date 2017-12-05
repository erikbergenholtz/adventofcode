import System.Environment
import System.IO
import Data.List

isValid :: [String] -> Int
isValid [] = 0
isValid xs
    | True `elem` uniq = 0
    | otherwise        = 1
    where uniq         = map (elem' xs) xs
          elem' xs x   = elem x (delete x xs)


isValid2 :: [String] -> Int
isValid2 [] = 0
isValid2 xs
    | True `elem` uniq = 0
    | otherwise        = 1
    where uniq         = map (elem' xs) xs
          elem' xs x   = elem (sort x) $ map sort (delete x xs)

main :: IO()
main = do
    args <- getArgs
    f <- openFile (head args) ReadMode
    contents <- hGetContents f
    let ls = map words (lines contents)
    putStrLn $ show $ sum $ map isValid ls
    putStrLn $ show $ sum $ map isValid2 ls
