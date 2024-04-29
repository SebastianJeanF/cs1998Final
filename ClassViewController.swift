import Foundation
import UIKit

class CardBackViewController: UIViewController {
    
    // MARK: - Properties
    
    var card: Card?

    private let answerLabel = UILabel()
    // MARK: - UI Elements
    
    // MARK: - Lifecycle Methods
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = UIColor.white
        setupLabels()
        populateData()
    }
    
    // MARK: - Private Methods
    
    private func setupLabels(){
        answerLabel.textColor = UIColor.black
       answerLabel.font = UIFont.boldSystemFont(ofSize: 24)
       answerLabel.numberOfLines = 0
        answerLabel.lineBreakMode = .byWordWrapping
        answerLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(answerLabel)
        NSLayoutConstraint.activate([
            answerLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            answerLabel.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])
    }

    
    private func populateData() {
        guard let card = card else { return }
        answerLabel.text = card.answer
    }
}
