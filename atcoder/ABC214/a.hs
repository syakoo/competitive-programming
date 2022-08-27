main :: IO ()
main = print . f =<< readLn

f :: Int -> Int
f x
  | x < 126 = 4
  | x < 212 = 6
  | otherwise = 8
