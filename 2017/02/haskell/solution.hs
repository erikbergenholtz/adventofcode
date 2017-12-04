import System.Environment
import System.IO
import Data.Char

arrayRead :: [[String]] -> [[Int]]
arrayRead [] = []
arrayRead (xs:xss) = (map read xs) : arrayRead xss

rowSum :: [Int] -> Int
rowSum []  = 0
rowSum xs  = abs ((maximum xs) - (minimum xs))

findDivisible :: [Int] -> Int -> Int
findDivisible _  0 = 0
findDivisible [] _ = 0
findDivisible (y:ys) x
    | x == y         = findDivisible ys x
    | h `rem` l == 0 = h `quot` l
    | otherwise      = findDivisible ys x
    where h          = max x y
          l          = min x y

part2 :: [Int] -> Int
part2 (x:xs)
    | res > 0   = res
    | otherwise = part2 xs
    where res   = findDivisible xs x

main :: IO()
main = do
    args <- getArgs
    f <- openFile (head args) ReadMode
    contents <- hGetContents f
    let ls = arrayRead $ map words $ lines contents
    -- Part 1
    putStrLn $ show $ sum $ map rowSum ls
    -- Part 2
    putStrLn $ show $ sum $ map part2 ls
