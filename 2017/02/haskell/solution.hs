import System.Environment
import System.IO
import Data.Char
import Data.List

rowSum :: [String] -> Int
rowSum []  = 0
rowSum xs  = abs ((maximum nums) - (minimum nums))
    where nums = map read xs

main :: IO()
main = do
    args <- getArgs
    f <- openFile (head args) ReadMode
    contents <- hGetContents f
    putStrLn $ show $ sum $ map rowSum (map words ( lines contents ))
