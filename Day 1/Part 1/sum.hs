intToStr :: String -> Integer
intToStr x = read x :: Integer


parseString :: String -> Integer
parseString x
    | head x == '+' = intToStr $ tail x
    | head x == '-' = -1 * (intToStr $ tail x)

main :: IO ()
main = do
    fileData <- readFile "input"
    let line = lines fileData
    let numbers = map parseString line
    print $ sum numbers