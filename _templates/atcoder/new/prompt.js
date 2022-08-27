module.exports = {
  prompt: ({ inquirer, args }) => {
    const questions = [
      {
        type: 'input',
        name: 'fileRange',
        message: '生成する Python ファイルの範囲は？ (例: b-e)',
      },
    ]
    return inquirer.prompt(questions).then((answers) => {
      const { fileRange } = answers
      const { name } = args
      const result = {
        fileDir: `atcoder/${name}`,
      }

      if (`${fileRange}`.includes('-')) {
        const alphas = 'abcdefghijklmnopqrstu'.split('')
        const start = fileRange.split('-')[0].trim().toLowerCase()
        const end = fileRange.split('-')[1].trim().toLowerCase()

        result.files = alphas
          .splice(
            alphas.findIndex((a) => a === start),
            alphas.findIndex((a) => a === end)
          )
          .map((f) => `${result.fileDir}/${f}.py`)
          .join(' ')
      }

      return result
    })
  },
}
