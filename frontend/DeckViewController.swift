import Foundation
import UIKit

struct Card : Decodable{
    let id: String
    let question: String
    let answer: String
}


class CardFrontView: UICollectionViewCell{

    let questionLabel = UILabel()

    static let reuse = "CardFrontViewReuse"

       // MARK: - init

       override init(frame: CGRect) {
           super.init(frame: frame)
           setupLabels()
       }

       required init?(coder: NSCoder) {
           fatalError("init(coder:) has not been implemented")
       }

       // MARK: - configure

    func configure(post : Card) {
        print("hello")
        questionLabel.text = post.question
       }

       // MARK: - Set Up Views

       private func setupLabels() {
           questionLabel.textColor = UIColor.black
           backgroundColor = UIColor.lightGray
           questionLabel.font = .systemFont(ofSize: 15, weight: .medium)
           questionLabel.numberOfLines = 0
           questionLabel.lineBreakMode = .byWordWrapping
           questionLabel.translatesAutoresizingMaskIntoConstraints = false
           contentView.addSubview(questionLabel)
           NSLayoutConstraint.activate([
               questionLabel.centerXAnchor.constraint(equalTo: contentView.centerXAnchor),
               questionLabel.centerYAnchor.constraint(equalTo: contentView.centerYAnchor)
           ])
       }
}
