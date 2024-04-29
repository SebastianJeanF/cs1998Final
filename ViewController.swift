//
//  ViewController.swift
//  hack_challenge
//
//  Created by Yinuo Tang on 4/27/24.
//


import UIKit
class ViewController: UIViewController {

    // MARK: - Properties (view)

    private var collectionView1: UICollectionView!

       // MARK: - Properties (data)

    static var dummyData = [
        Card(id: "a", question: "q1", answer: "a1"),
        Card(id: "b", question: "q2", answer: "a2"),
        Card(id: "c", question: "q3", answer: "a3")
    ]

       // MARK: - viewDidLoad
//    @objc private func fetchRoster() {
//        NetworkManager.shared.fetchRoster { [weak self] posts in
//            guard let self = self else { return }
//            ViewController.dummyData = posts
//
//            // Perform UI update on main queue
//            DispatchQueue.main.async {
//                self.collectionView1.reloadData()
//            }
//        }
//    }

       override func viewDidLoad() {
           super.viewDidLoad()
           title = "Cards"
           view.backgroundColor = UIColor.lightGray

           setupCollectionView()
           collectionView1.alwaysBounceVertical = true
//           fetchRoster()
       }

       // MARK: - Set Up Views
    
       private func setupCollectionView() {
           let layout = UICollectionViewFlowLayout()
           layout.scrollDirection = .vertical
           layout.minimumLineSpacing = 16
           layout.minimumInteritemSpacing = 16
           collectionView1 = UICollectionView(frame: .zero, collectionViewLayout: layout)
           collectionView1.register(CardFrontView.self, forCellWithReuseIdentifier: CardFrontView.reuse)
           collectionView1.delegate = self
           collectionView1.dataSource = self
           collectionView1.translatesAutoresizingMaskIntoConstraints = false
           view.addSubview(collectionView1)
           NSLayoutConstraint.activate([
               collectionView1.topAnchor.constraint(equalTo: view.topAnchor),
               collectionView1.leadingAnchor.constraint(equalTo: view.leadingAnchor),
               collectionView1.bottomAnchor.constraint(equalTo: view.bottomAnchor),
               collectionView1.trailingAnchor.constraint(equalTo: view.trailingAnchor)
           ])
       }
   }

   // MARK: - UICollectionView DataSource

extension ViewController: UICollectionViewDataSource {
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        if(collectionView == collectionView1){
            return ViewController.dummyData.count
        }
        return ViewController.dummyData.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        print("cellforitemat")
        guard let cell = collectionView.dequeueReusableCell(withReuseIdentifier: CardFrontView.reuse, for: indexPath) as? CardFrontView else { return UICollectionViewCell() }
        let card = ViewController.dummyData[indexPath.item]
        cell.configure(post: card)
        return cell
    }
}

   // MARK: - UICollectionViewDelegateFlowLayout

   extension ViewController: UICollectionViewDelegateFlowLayout {

       func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
               let size = collectionView.frame.width / 2 - 16
               return CGSize(width: size, height: size)}
       }


   // MARK: - UICollectionViewDelegate

extension ViewController: UICollectionViewDelegate {
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {

            let selected = ViewController.dummyData[indexPath.item]
            let cardbController = CardBackViewController()
            cardbController.card = selected
            navigationController?.pushViewController(cardbController, animated: true)
            collectionView.reloadData()
        }
    }

