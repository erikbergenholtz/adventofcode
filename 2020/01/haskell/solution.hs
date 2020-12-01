import System.IO
import System.Environment
import Data.Char
import Data.Typeable
import Data.List

solve :: [Int] -> Int
solve xs = test xs xs (tail xs)

test :: [Int] -> [Int] -> [Int] -> Int
test [] _ _ = -1
test (x:xs) [] (y:ys) = test xs ys (tail ys)
test (x:xs) (y:ys) ys'
    | x + y == 2020 = x*y
    | otherwise     = test (x:xs) ys ys'

main :: IO()
main = do
    argv     <- getArgs
    file     <- openFile (head argv) ReadMode
    contents <- hGetContents file
    let ds = sort $ map read (words contents) :: [Int]
    putStrLn $ show $ solve ds
