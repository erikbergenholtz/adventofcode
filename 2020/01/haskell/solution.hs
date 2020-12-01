import System.IO
import System.Environment
import Data.Char
import Data.Typeable
import Data.List

solve :: [Int] -> (Maybe Int)
solve xs = test xs xs (tail xs)

test :: [Int] -> [Int] -> [Int] -> (Maybe Int)
test [] _ _ = Nothing
test (x:xs) [] (y:ys) = test xs ys (tail ys)
test (x:xs) (y:ys) ys'
    | x + y == 2020 = (Just (x*y))
    | otherwise     = test (x:xs) ys ys'

solve2 :: [Int] -> (Maybe Int)
solve2 xs = test2 xs xs xs (tail xs) (tail xs)

test2 :: [Int] -> [Int] -> [Int] -> [Int] -> [Int] -> (Maybe Int)
test2 [] _ _ _ _ = Nothing
test2 (x:xs) [] [] ys' zs'  = test2 xs ys' zs' ys' zs'
test2 (x:xs) [] (z:zs) ys' zs'  = test2 xs ys' zs' ys' zs'
test2 (x:xs) (y:ys) [] ys' zs'  = test2 (x:xs) ys zs' ys' zs'
test2 (x:xs) (y:ys) (z:zs) ys' zs'
    | x + y + z == 2020 = (Just (x*y*z))
    | otherwise     = test2 (x:xs) (y:ys) zs ys' zs'

main :: IO()
main = do
    argv     <- getArgs
    file     <- openFile (head argv) ReadMode
    contents <- hGetContents file
    let ds = sort $ map read (words contents) :: [Int]
    putStrLn $ show $ solve ds
    putStrLn $ show $ solve2 ds
